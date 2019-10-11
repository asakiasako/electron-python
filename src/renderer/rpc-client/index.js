import zeroRPC from 'zerorpc'
import {remote} from 'electron'

const getRpcPort = remote.getGlobal('getRpcPort')

/* get current port from main process */
const clientIP = '127.0.0.1'
const clientPort = getRpcPort()

/* run RPC client */
export const rpcClient = new zeroRPC.Client()

rpcClient.connectServer = function (address) {
  let client = this
  console.log(`tcp://${address}:${clientPort}`)
  client.connect(`tcp://${address}:${clientPort}`)
}

rpcClient.disconnectServer = function (address) {
  let client = this
  client._socket._zmqSocket.disconnect(`tcp://${address}:${clientPort}`)
}

rpcClient.invokes = function (...args) {
  return new Promise(function (resolve, reject) {
    rpcClient.invoke(...args, (err, res, more) => {
      if (err) {
        reject(err)
      } else {
        resolve(res)
      }
    })
  })
}

rpcClient.request = function (params) {
  return rpcClient.invokes('request', params)
}

rpcClient.checkConnection = function () {
  return rpcClient.invokes('check_connection')
}

rpcClient.connectServer(clientIP)
