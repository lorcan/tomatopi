import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'

export default function Layout({ children }) {
  return (
    <div className={styles.container}>
      <Head>
        <title>Raspberry Pi</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Raspberry Pi!</h1>
        {children}
      </main>

      <footer className={styles.footer}>
        <Link href="/">
          <a>Home</a>
        </Link>
        <Link href="/camera">
          <a>Camera</a>
        </Link>
        <Link href="/pijuice">
          <a>PiJuice</a>
        </Link>
      </footer>
    </div>
  )
}
