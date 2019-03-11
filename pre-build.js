const fs = require('fs')

// === Add Build Version == //
let jsonStr = fs.readFileSync('package.json')
let packageConfig = JSON.parse(jsonStr)
packageConfig.version = packageConfig.version.replace(/-Build.*/, '')
packageConfig.version = `${packageConfig.version}-Build${((new Date().getTime() - 1546272000000) / 100).toFixed()}`
let modJsonStr = JSON.stringify(packageConfig, null, 2)
fs.writeFileSync('package.json', modJsonStr)

