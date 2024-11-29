import React from 'react';
import { Providers } from './providers';
import { AppRouter } from './router';

interface ApplicationProps {}

export const Application: React.FC<ApplicationProps> = () => {
  return (
    <Providers>
      <AppRouter />
    </Providers>
  );
};
