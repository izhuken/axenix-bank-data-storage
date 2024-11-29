import { Header, LogoutLayout } from '@/components';
import React from 'react';

interface LogOutProps {}

export const LogOut: React.FC<LogOutProps> = () => {
  return (
    <>
      <Header />
      <LogoutLayout />
    </>
  );
};
