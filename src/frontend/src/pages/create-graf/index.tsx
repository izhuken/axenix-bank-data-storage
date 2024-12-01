import { API_SERVER_URL } from '@/assets';
import { PieChart } from '@/components/charts/pie-chart';
import { ChoiseGrafModal } from '@/components/choise-graf';
import { Header } from '@/components/header';
import { Flex, Grid, GridItem, Heading, Input } from '@chakra-ui/react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import React, { useState } from 'react';
import { Helmet } from 'react-helmet';

interface CreateGrafProps {}

export type ChartFormData = {
  chartType: 'pie' | 'area' | 'column';
  reportName?: string;
  payload: { value: number; title: string }[];
};

export const CreateGraf: React.FC<CreateGrafProps> = () => {
  const [page, setPage] = useState({});
  const {} = useQuery({
    queryKey: ['table-payload', page],
    queryFn: async () => {
      const first_decade = await axios.get(`${API_SERVER_URL}/`, {
        params: {
          ...page,
          created_at_from: '1990-01-01',
          created_at_to: '1999-12-31',
        },
      });
      const second_decade = await axios.get(`${API_SERVER_URL}/`, {
        params: {
          ...page,
          created_at_from: '2000-01-01',
          created_at_to: '2010-12-31',
        },
      });
      const third_decade = await axios.get(`${API_SERVER_URL}/`, {
        params: {
          ...page,
          created_at_from: '2010-01-01',
          created_at_to: '2020-12-31',
        },
      });
    },
  });

  return (
    <>
      <Helmet>
        <title>Графики | Lab of Dev</title>
      </Helmet>
      <Header />

      <Grid
        gridTemplateColumns={'300px 1fr'}
        width={'100dvw'}
        p={'40px'}
        gap={10}
        height={'calc(100dvh - 60px)'}
      >
        <GridItem>
          <ChoiseGrafModal updatePage={setPage} />
        </GridItem>
        <GridItem
          as={Flex}
          align={'center'}
          justify={'center'}
          border={'2px solid #B1B1B1'}
          borderRadius={'10px'}
          flexFlow={'column'}
          p={'20px 40px'}
        >
          <Heading w={'100%'}>
            <Input
              placeholder='Введите название графика'
              border={'none'}
              borderBottom={'1px solid #B1B1B1'}
              borderRadius={0}
              p={0}
              css={{
                '&:focus-visible': {
                  boxShadow: 'none',
                },
              }}
              mb={5}
            />
          </Heading>

          <PieChart />
        </GridItem>
      </Grid>
    </>
  );
};
