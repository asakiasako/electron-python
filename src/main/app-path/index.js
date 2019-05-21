import {appData} from './constants'
import {app} from 'electron'
import path from 'path'

let appName = app.getName()
if (process.env.NODE_ENV === 'development') {
  const fs = require('fs')
  let jsonStr = fs.readFileSync('package.json')
  appName = JSON.parse(jsonStr).productName + '_DEV'
}
let userData = path.join(appData, appName)

app.setPath('appData', appData)
app.setPath('userData', userData)
app.setPath('logs', path.join(userData, 'Logs'))
