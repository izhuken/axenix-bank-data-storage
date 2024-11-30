import { UsersStyles } from '@/assets';
import { Header } from '@/components/header';
import { TableForm } from '@/components/table/table';
import { Tab, TabList, TabPanel, TabPanels, Tabs } from '@chakra-ui/react';
import React from 'react';

interface UserProfileProps {}
export const UserProfile: React.FC<UserProfileProps> = () => {
  return (
    <>
      <Header />
      <div className={UsersStyles.conteiner_table}>
        <div className={UsersStyles.content_table}>
          <div className={UsersStyles.table_btn}>
            <Tabs w={'100%'}>
              <TabList>
                <Tab>Загруженные отчеты</Tab>
                <Tab>Созданные отчеты</Tab>
              </TabList>

              <TabPanels w={'100%'}>
                <TabPanel w={'100%'}>
                  <TableForm />
                </TabPanel>
                <TabPanel>
                  <TableForm />
                </TabPanel>
              </TabPanels>
            </Tabs>
          </div>
        </div>
      </div>
    </>
  );
};
