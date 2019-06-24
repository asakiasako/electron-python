/**
 * Settings of RPC
 */
const { DEFAULT_SERVER_PORT, PYTHON_PATH, PROCESS_PATH } = require('./const')
const portIsOccupied = require('./checkPort')

let rpcServer, rpcPort
let serverProcessAlive = false
let userDataPath = require('electron').app.getPath('userData')

const createRpcServer = () => {
  portIsOccupied(DEFAULT_SERVER_PORT).then(port => {
    if (process.env.NODE_ENV !== 'production') {
      rpcServer = require('child_process').spawn(PYTHON_PATH, [PROCESS_PATH, port])
      rpcServer.stdout.pipe(process.stdout)
      rpcServer.stderr.pipe(process.stderr)
    } else {
      rpcServer = require('child_process').execFile(PROCESS_PATH, [port])
    }
    if (rpcServer !== null) {
      console.log(`RPC server running on port ${port}`)
      console.log(`userData dir: ${userDataPath}`)
      serverProcessAlive = true
      rpcPort = port
      rpcServer.on('close', () => {
        rpcPort = undefined
        serverProcessAlive = false
        rpcServer = null
      })
    }
  }).catch(err => {
    // TODO: error management
    console.log(err)
  })
}

const exitRpcServer = () => {
  if (rpcServer && isServerProcessAlive()) {
    rpcServer.kill()
  }
}

const getRpcPort = () => {
  return rpcPort
}

const isServerProcessAlive = () => {
  return serverProcessAlive
}

module.exports = {
  createRpcServer,
  exitRpcServer,
  getRpcPort,
  isServerProcessAlive
}
