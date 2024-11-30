import { UsersStyles } from '@/assets';
import { ModalLoad } from '@/components/load-modal';
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
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <>
      <div className={UsersStyles.all_table}>
        <hr />
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
                    <Button onClick={onOpen}>
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
