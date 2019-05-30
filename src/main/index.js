'use strict'

import { app, BrowserWindow, globalShortcut } from 'electron'
import './app-path'
import {acceleratorMap} from './accelerator'

/**
 * Set `__static` path to static files in production
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html
 */
if (process.env.NODE_ENV !== 'development') {
  global.__static = require('path').join(__dirname, '/static').replace(/\\/g, '\\\\')
}

const { createRpcServer, exitRpcServer, getRpcPort } = require('./rpc-server')
require('./menu')

const winURL = process.env.NODE_ENV === 'development'
  ? `http://localhost:9080`
  : `file://${__dirname}/index.html`

/**
 * Set global names
 */
global.getRpcPort = getRpcPort

/**
 * make single instance
 */

let mainWindow = null

const gotTheLock = app.requestSingleInstanceLock()

if (!gotTheLock) {
  app.quit()
} else {
  app.on('second-instance', (event, commandLine, workingDirectory) => {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore()
      mainWindow.focus()
    }
  })
}

/**
 * window initialize
 */

createRpcServer()

function createWindow () {
  mainWindow = new BrowserWindow({
    title: app.getName(),
    useContentSize: true,
    width: 1280,
    height: 720,
    minWidth: 1280,
    minHeight: 720
  })

  mainWindow.loadURL(winURL)

  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

function registerAccelerators () {
  for (let key in acceleratorMap) {
    globalShortcut.register(key, () => {
      acceleratorMap[key](mainWindow)
    })
  }
}

/**
 * app lifecycle
 */

app.on('ready', () => {
  createWindow()
  registerAccelerators()
})

app.on('will-quit', () => {
  exitRpcServer()
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})

/**
 * Auto Updater
 *
 * Uncomment the following code below and install `electron-updater` to
 * support auto updating. Code Signing with a valid certificate is required.
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-electron-builder.html#auto-updating
 */

/*
import { autoUpdater } from 'electron-updater'

autoUpdater.on('update-downloaded', () => {
  autoUpdater.quitAndInstall()
})

app.on('ready', () => {
  if (process.env.NODE_ENV === 'production') autoUpdater.checkForUpdates()
})
 */
