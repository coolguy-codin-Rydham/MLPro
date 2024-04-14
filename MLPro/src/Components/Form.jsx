import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup"
import { useRef } from "react";
const Form = ({setQuery}) => {

    const formRef = useRef()
  

  const schema = yup.object().shape({
    Date: yup.string().required(),
    Hour: yup.number().required(),
    Temperature: yup.number().required(),
    Humidity: yup.number().required(),
    WindSpeed: yup.number().required(),
    Visibility: yup.number().required(),
    SolarRadiation: yup.number().required(),
    Rainfall:yup.number().required(),
    Snowfall:yup.number().required(),
    Season:yup.string().required().oneOf(["Winter", "Summer", "Spring"]),
    Holiday:yup.string().required().oneOf(["Holiday", "No Holiday"]),
    Functioning:yup.string().required().oneOf(["Yes", "No"]),
  });

  const { register, handleSubmit } = useForm({
    resolver:yupResolver(schema)
  });

  const onSubmit = (data) => {  
    console.log(data)
    formRef.current.reset()
    setQuery(data);
  };
  return (
    <form
        ref={formRef}

      onSubmit={handleSubmit(onSubmit)}
      className="grid grid-cols-2 gap-6 px-4 py-4 border-2 border-black rounded-lg backdrop-blur-lg bg-white/20"
    >
      <label htmlFor="" className="flex flex-col">
        Date
        <input
          className="px-1 py-1 rounded-md"
          type="text"
          placeholder="Enter Date (DD/MM/YY)"
          {...register("Date")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Hour
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          placeholder="Enter Hour (0-23)"
          {...register("Hour")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Temperature
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          placeholder="Enter Temperature in ℃"
          {...register("Temperature")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Humidity
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          placeholder="Enter Humidity"
          {...register("Humidity")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Wind Speed
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          placeholder="Enter Wind Speed"
          {...register("WindSpeed")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Visibility
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          placeholder="Enter Visibility"
          {...register("Visibility")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Solar Radiation
        <input
          className="px-1 py-1 rounded-md"
          step="0.1"
          type="number"
          placeholder="Enter Solar Radiation"
          {...register("SolarRadiation")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Rainfall
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          step="0.1"
          placeholder="Enter Rainfall"
          {...register("Rainfall")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Snowfall
        <input
          className="px-1 py-1 rounded-md"
          type="number"
          placeholder="Enter Snowfall"
          step="0.1"
          {...register("Snowfall")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Season
        <input
          className="px-1 py-1 rounded-md"
          type="text"
          placeholder="Enter Season"
          {...register("Season")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Holiday
        <input
          className="px-1 py-1 rounded-md"
          type="text"
          placeholder="Enter Holiday(Holiday/No Holiday)"
          {...register("Holiday")}
        />
      </label>
      <label htmlFor="" className="flex flex-col">
        Functioning
        <input
          className="px-1 py-1 rounded-md"
          type="text"
          placeholder="Enter Functioning Day (Yes/ No)"
          {...register("Functioning")}
        />
      </label>
      <input className="col-start-1 col-end-3 px-1 py-1 rounded-md" type="submit" />
    </form>
  );
};

export default Form;
