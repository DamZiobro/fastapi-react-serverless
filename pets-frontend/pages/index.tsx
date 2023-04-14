import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState<any>([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/hello");
      const data = await response.json();
      setData(data);
    }

    fetchData();
  }, []);

  return (
    <div>
      <div>Data from API:</div>
      <div>
          {data ? <p>{data.message!}</p> : <p>Loading...</p>}
     </div>
    </div>
  );
}
