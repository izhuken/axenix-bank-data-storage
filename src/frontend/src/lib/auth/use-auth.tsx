import React, { ReactNode } from 'react';

interface IsAuthenticatedProtectionProps {
  children: ReactNode;
}

export const IsAuthenticatedProtection: React.FC<
  IsAuthenticatedProtectionProps
> = ({ children }) => {
  // useEffect(() => {
  //   useAuthentication().then((response) => {
  //     if (!response) navigate('/sign-in');
  //     return;
  //   });
  // });

  return <>{children}</>;
};
