const { spawn } = require('child_process')

export default (req, res) => {
  let dataToSend
  let process = spawn('python', ['scripts/pi_juice.py'])

  process.stdout.on('data', (data) => {
    console.info(`got data: ${data}`)
    dataToSend = data.toString()
  })

  process.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`)
    res.statusCode = 200
    res.setHeader('Content-Type', 'application/json')
    res.send(dataToSend)
  })
}
