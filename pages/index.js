import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Raspberry Pi</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Raspberry Pi!</h1>

        <button onClick={() => fetch(`/api/photo`)}>Take photo</button>
      </main>

      <footer className={styles.footer}>
        <Link href="/pijuice">PiJuice</Link>
      </footer>
    </div>
  )
}
