import React from 'react';
import img from '../../../public/pie.svg';

interface pieProp {}
export const Pie: React.FC<pieProp> = () => {
  return (
    <>
      <img src={img} width={20} />
    </>
  );
};
