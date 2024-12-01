import { Pie } from '@ant-design/charts';

import React, { useMemo } from 'react';

interface PieChartProps {}
export const PieChart: React.FC<PieChartProps> = () => {
  const chartData = useMemo(
    () => [
      { type: 'ауе 1', value: 27 },
      { type: 'ауе 2', value: 25 },
      { type: 'ауе 3', value: 18 },
      { type: 'ауе 4', value: 15 },
      { type: 'ауе 5', value: 10 },
      { type: 'ауе 6', value: 5 },
    ],
    [],
  );

  return (
    <>
      <Pie
        data={chartData}
        angleField={'value'}
        colorField={'type'}
        label={{
          text: 'value',
          style: {
            fontWeight: 'bold',
          },
        }}
        legend={{
          color: {
            title: false,
            position: 'right',
            rowPadding: 5,
          },
        }}
      />
    </>
  );
};
