import React, { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const CompanyChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/analytics/company")   // <--- your endpoint
      .then(res => res.json())
      .then(data => {
        const companies = data.companies.map(item => item.company);
        const counts = data.companies.map(item => item.count);

        setChartData({
          labels: companies,
          datasets: [
            {
              label: "Alumni per Company",
              data: counts,
              backgroundColor: "rgba(75, 192, 192, 0.6)",
            }
          ]
        });
      })
      .catch(err => console.error("Failed to load API:", err));
  }, []);

  if (!chartData) return <p>Loading chart...</p>;

  return (
    <div style={{ width: "600px", margin: "50px auto" }}>
      <Bar data={chartData} />
    </div>
  );
};

export default CompanyChart;
