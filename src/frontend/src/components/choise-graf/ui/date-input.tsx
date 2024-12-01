import { Input, InputProps } from '@chakra-ui/react';
import React, { useRef } from 'react';

interface DateInputProps extends InputProps {}

export const DateInput: React.FC<DateInputProps> = (props) => {
  const ref = useRef<HTMLInputElement | null>(null);

  return (
    <>
      <Input {...props} border={'1px solid #B1B1B1'} type='date' ref={ref} />
    </>
  );
};
