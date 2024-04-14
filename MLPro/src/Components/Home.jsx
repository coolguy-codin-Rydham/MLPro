import Form from "./Form"

const Home = ({setQuery, query}) => {
  return (
    <div className="h-screen flex items-center justify-center">
        <Form setQuery={setQuery} query={query}/>
    </div>
  )
}

export default Home
