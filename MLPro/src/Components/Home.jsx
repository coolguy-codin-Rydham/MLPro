import Form from "./Form"

const Home = ({setQuery, query}) => {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="pb-10 text-4xl font-bold text-center ">Ola Bike Ride Request <br /> Demand Forecast</h1>
        <Form setQuery={setQuery} query={query}/>
    </div>
  )
}

export default Home
