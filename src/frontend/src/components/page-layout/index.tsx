import { Grid, GridItem } from '@chakra-ui/react';
import { FC, ReactNode } from 'react';

interface PageLayoutProps {
  children: ReactNode;
}

export const PageLayout: FC<PageLayoutProps> = ({ children }) => {
  return (
    <Grid w={'100dvw'} h={'100dvh'}>
      <GridItem>{children}</GridItem>
    </Grid>
  );
};
