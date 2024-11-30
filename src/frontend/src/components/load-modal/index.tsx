import {
  Box,
  Button,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Text,
} from '@chakra-ui/react';
import React from 'react';

interface ModalLoadProps {
  isOpen: boolean;
  onClose: () => void;
}

export const ModalLoad: React.FC<ModalLoadProps> = ({ isOpen, onClose }) => {
  return (
    <>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader textAlign='center'>Загрузка отчета</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormLabel mt={4} variant={'events'} htmlFor='newUser'>
              <Text fontSize='12px' mb='4px'>
                Загрузить фото
              </Text>
              <Box
                display='flex'
                flexDirection='column'
                alignItems='center'
                justifyContent='center'
                border='0.5px solid black '
                width={400}
                height={200}
                borderRadius={8}
              >
                <Box
                  display='flex'
                  flexDirection='column'
                  alignItems='center'
                  justifyContent='center'
                >
                  <img src='/load-icon.svg' width={100} />
                  <Text fontSize='12px'>Добавить файл</Text>
                </Box>
              </Box>
            </FormLabel>
            <Input display={'none'} type='file' id='newUser' />
          </ModalBody>
          <ModalFooter
            width='100%'
            display='flex'
            flexDirection='column'
            alignItems='baseline'
            justifyContent='center'
          >
            <Button
              bgColor='rgba(255, 86, 2, 1)'
              colorScheme='orange'
              width='400px'
            >
              Загрузить
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
};
