import { Area } from '@ant-design/plots';
import React from 'react';

interface AreaChartProps {}
export const AreaChart: React.FC<AreaChartProps> = () => {
  const config = {
    data: {
      type: 'fetch',
      value: 'https://assets.antv.antgroup.com/g2/aapl.json',
    },
    xField: (d) => new Date(d.date),
    yField: 'close',
  };

  return (
    <>
      <Area {...config} />
    </>
  );
};
