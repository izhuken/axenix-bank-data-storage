import { theme } from '@/lib';
import { RootStoreContext } from '@/lib/hooks/use-store';
import { RootStore } from '@/storage';
import { ChakraProvider } from '@chakra-ui/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import React, { ReactNode } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { ToastProvider } from './lib';

interface ProvidersProps {
  children: ReactNode;
}

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
});

export const Providers: React.FC<ProvidersProps> = ({ children }) => {
  return (
    <React.StrictMode>
      <ToastProvider>
        <QueryClientProvider client={queryClient}>
          <RootStoreContext.Provider value={RootStore}>
            <BrowserRouter>
              <ChakraProvider value={theme}>{children}</ChakraProvider>
            </BrowserRouter>
          </RootStoreContext.Provider>
        </QueryClientProvider>
      </ToastProvider>
    </React.StrictMode>
  );
};
