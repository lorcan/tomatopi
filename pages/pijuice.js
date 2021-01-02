import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function PiJuice(props) {
  return (
    <div className={styles.container}>
      <Head>
        <title>PiJuice</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
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
      </main>

      <footer className={styles.footer}></footer>
    </div>
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
