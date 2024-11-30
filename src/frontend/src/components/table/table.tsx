import { UsersStyles } from '@/assets';
import { ModalLoad } from '@/components/load-modal';
import { UserStoreInstance } from '@/storage/store';
import { AddIcon } from '@chakra-ui/icons';
import {
  Button,
  Table,
  TableCaption,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
  useDisclosure,
} from '@chakra-ui/react';
import React from 'react';

interface TableFromProps {}
export const TableForm: React.FC<TableFromProps> = () => {
  const user = UserStoreInstance.user;
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <>
      <div className={UsersStyles.all_table}>
        <div className={UsersStyles.table_title}>
          <p>Выбран пользователь : {user?.name}</p>
        </div>

        <div className={UsersStyles.table}>
          <TableContainer>
            <Table border='1px solid rgba(227, 206, 170, 1)'>
              <TableCaption
                className={UsersStyles.field}
                border='1px solid rgba(227, 206, 170, 1)'
              >
                {/* <Pagination count={10} variant='outlined' color='primary' /> */}
              </TableCaption>
              <Thead className={UsersStyles.field}>
                <Tr>
                  <Th border='1px solid rgba(227, 206, 170, 1)'>Название</Th>
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
                <Tr>
                  <Td border='0px solid rgba(227, 206, 170, 1)'></Td>
                  <Td border='0px solid rgba(227, 206, 170, 1)'>
                    <Button
                      marginLeft={20}
                      bgColor='rgba(255, 86, 2, 1)'
                      colorScheme='orange'
                      onClick={onOpen}
                    >
                      <AddIcon />
                    </Button>
                  </Td>
                </Tr>
              </Tbody>
            </Table>
          </TableContainer>
          <ModalLoad onClose={onClose} isOpen={isOpen} />
        </div>
      </div>
    </>
  );
};
