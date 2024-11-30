import { CredentialStorage, UsersStyles } from '@/assets';
import { authApi } from '@/assets/config/api';
import { Header } from '@/components/header';
import { TableForm } from '@/components/table/table';
import { User } from '@/entities';
import { UserStoreInstance } from '@/storage/store';
import { Tab, TabList, TabPanel, TabPanels, Tabs } from '@chakra-ui/react';
import axios from 'axios';
import { observer } from 'mobx-react-lite';
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

interface UserProfileProps {}
export const UserProfile: React.FC<UserProfileProps> = observer(() => {
  const user = UserStoreInstance.user;
  const nav = useNavigate();

  useEffect(() => {
    if (!user && CredentialStorage.get('access')) {
      axios
        .get<User>(`${authApi}/user`, {
          headers: {
            Authorization: `Bearer ${CredentialStorage.get('access')}`,
          },
        })
        .then((data) => {
          if (!data.data) {
            return nav('/login');
          }

          UserStoreInstance.user = data.data;
        })
        .catch(() => {
          nav('/login');
        });
      return;
    }
  }, [user]);

  return (
    <>
      <Header />
      <div className={UsersStyles.conteiner_table}>
        <div className={UsersStyles.content_table}>
          <div className={UsersStyles.table_btn}>
            <Tabs w={'100%'} variant='soft-rounded' colorScheme='orange'>
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
});
