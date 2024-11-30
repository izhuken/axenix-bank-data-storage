import { UsersStyles } from '@/assets';
import { Header } from '@/components/header';
import { ModalLoad } from '@/components/load-modal';
import { AddIcon } from '@chakra-ui/icons';
import {
  Button,
  Table,
  TableCaption,
  TableContainer,
  Tbody,
  Td,
  Tfoot,
  Th,
  Thead,
  Tr,
  useDisclosure,
} from '@chakra-ui/react';
import React from 'react';

interface UserProfileProps {}
export const UserProfile: React.FC<UserProfileProps> = () => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <>
      <Header />
      <div className={UsersStyles.conteiner_table}>
        <div className={UsersStyles.content_table}>
          <div className={UsersStyles.table_btn}>
            <Button>Загруженные отчеты</Button>
            <Button>Созданные отчеты</Button>
          </div>
          <hr />
          <div className={UsersStyles.all_table}>
            <div className={UsersStyles.table_title}>
              <p>Выбран пользователь : Долбаебов Е.Ш.</p>
            </div>

            <div className={UsersStyles.table}>
              <TableContainer>
                <Table border='1px solid rgba(227, 206, 170, 1)'>
                  <TableCaption
                    className={UsersStyles.field}
                    border='1px solid rgba(227, 206, 170, 1)'
                  >
                    Imperial to metric conversion factors
                  </TableCaption>
                  <Thead className={UsersStyles.field}>
                    <Tr>
                      <Th border='1px solid rgba(227, 206, 170, 1)'>
                        Название
                      </Th>
                      <Th border='1px solid rgba(227, 206, 170, 1)'>
                        Дата загрузки
                      </Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    <Tr>
                      <Td border='1px solid rgba(227, 206, 170, 1)'>inches</Td>
                      <Td border='1px solid rgba(227, 206, 170, 1)'>
                        millimetres (mm)
                      </Td>
                    </Tr>
                  </Tbody>
                  <Tfoot>
                    <Tr display='flex' justifyContent='center'>
                      <Button onClick={onOpen}>
                        <AddIcon />
                      </Button>
                    </Tr>
                  </Tfoot>
                </Table>
              </TableContainer>
              <ModalLoad onClose={onClose} isOpen={isOpen} />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
