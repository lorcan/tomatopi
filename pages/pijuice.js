import Layout from '../components/layout.js'
import styles from '../styles/Home.module.css'

export default function PiJuice(props) {
  return (
    <Layout>
      <h1 className={styles.title}>Pi Juice</h1>
      <table>
        <thead>
          <th>Key</th>
          <th>Value</th>
        </thead>
        <tbody>
          {Object.keys(props.data).map((key) => (
            <tr>
              <td>
                <strong>{key}</strong>
              </td>
              <td>{JSON.stringify(props.data[key])}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </Layout>
  )
}

export async function getServerSideProps(context) {
  let res = await fetch('http://localhost:3000/api/pijuice')
  let data = await res.json()
  console.info(`getServerSideProps: ${data}`)
  return {
    props: { data },
  }
}
