const net = require('net')

function portIsOccupied (port) {
  console.log(`Checking port ${port} availability...`)
  const server = net.createServer().listen(port, '127.0.0.1')
  return new Promise((resolve, reject) => {
    server.on('listening', () => {
      server.close()
      resolve(port)
    })

    server.on('error', (err) => {
      if (err.code === 'EADDRINUSE') {
        console.log(`Port ${port} is occupied.`)
        resolve(portIsOccupied(port + 1)) // If occupied, add 1 and retry.
      } else {
        reject(err)
      }
    })
  })
}

module.exports = portIsOccupied
