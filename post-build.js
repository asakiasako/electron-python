const fs = require('fs')

fs.copyFileSync('package.json', 'package.build.json')

let jsonStr = fs.readFileSync('package.json')
let packageConfig = JSON.parse(jsonStr)
packageConfig.version = packageConfig.version.replace(/-Build.*/, '')
let modJsonStr = JSON.stringify(packageConfig, null, 2)
fs.writeFileSync('package.json', modJsonStr)
