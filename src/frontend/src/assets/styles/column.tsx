import React from 'react';
import img from '../../../public/column.svg';

interface ColumnProp {}
export const Column: React.FC<ColumnProp> = () => {
  return (
    <>
      <img src={img} width={20} />
    </>
  );
};
