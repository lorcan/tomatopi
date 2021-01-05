const { spawn } = require('child_process')

export default (req, res) => {
  spawn('python', ['scripts/camera.py'], { stdio: 'inherit' })
  res.statusCode = 200
  res.json({ name: 'Snap' })
}
