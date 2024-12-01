import { FormControl, FormLabel } from '@chakra-ui/react';
import React, { ReactNode } from 'react';

interface FilterFormControlProps {
  title: string;
  children: ReactNode;
}

export const FilterFormControl: React.FC<FilterFormControlProps> = ({
  children,
  title,
}) => {
  return (
    <FormControl w='100%'>
      <FormLabel mb={0} fontSize={12}>
        {title}
      </FormLabel>
      {children}
    </FormControl>
  );
};
