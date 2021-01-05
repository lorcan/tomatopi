import Layout from '../components/layout.js'

export default function Camera(props) {
  return (
    <Layout>
      <button onClick={() => fetch(`/api/photo`)}>Take photo</button>
      <img src="/photos/snap.jpg" height="400" alt="Last Image"></img>
    </Layout>
  )
}
