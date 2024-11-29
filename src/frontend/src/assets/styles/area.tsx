import React from 'react';
import img from '../../../public/area.svg';

interface AreaProp {}
export const Area: React.FC<AreaProp> = () => {
  return (
    <>
      <img src={img} width={20} />
    </>
  );
};
