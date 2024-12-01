import NewStyle from '@/assets/styles/new.module.scss';
import { Pie } from '@/assets/styles/pie';
import { Box, Button, HStack, Input, Text, VStack } from '@chakra-ui/react';
import { ErrorMessage } from '@hookform/error-message';
import React from 'react';
import { Controller, useForm } from 'react-hook-form';
import Select from 'react-select';
import { FormBaseLayout } from '../form-base-layout';
import { FilterFormControl } from './ui/filter-form-control';

interface ChoiseGrafModalProps {
  updatePage: (data: { [key: string]: string }) => { [key: string]: string };
}
export const ChoiseGrafModal: React.FC<ChoiseGrafModalProps> = () => {
  const form = useForm<{
    action_type: { label: string; value: string };
    target_field: { label: string; value: string };
    closed_at_from?: string;
    closed_at_to?: string;
    calculated_payment_number_from?: number;
    calculated_payment_number_to?: number;
    made_payments_from?: number;
    made_payments_to?: number;
    credit_sum_from?: number;
    credit_sum_to?: number;
  }>({
    defaultValues: {},
  });

  return (
    <>
      <VStack>
        <Text textAlign={'left'} w={'100%'}>
          Вид графика
        </Text>
        <Box className={NewStyle.group} mb={5}>
          <Button leftIcon={<Pie />} width={300} gap={1}>
            Пирог
          </Button>
        </Box>

        <Text textAlign={'left'} w={'100%'}>
          Фильтры
        </Text>
        <FormBaseLayout
          methods={form}
          onSub={(data) => {
            const totalPayload = {};

            Array.from(Object.entries(data)).forEach(([key, value]) => {
              if (!value) {
                return;
              }

              if (value?.value) {
                totalPayload[key] = value.value;
              } else {
                totalPayload[key] = value;
              }
            });

            console.log(data);
          }}
        >
          <VStack gap={3} className={NewStyle.group} mb={5} w='100%'>
            <FilterFormControl title='Операция'>
              <Controller
                control={form.control}
                name='action_type'
                rules={{
                  required: {
                    message: 'Обязательно выберите операцию',
                    value: true,
                  },
                }}
                render={({ field: { value, onChange } }) => (
                  <Select
                    value={value}
                    onChange={onChange}
                    styles={{
                      container: (provided) => ({
                        ...provided,
                        width: '100%',
                      }),
                    }}
                    placeholder='Выберите операцию'
                    options={[
                      {
                        value: 'sum',
                        label: 'Сумма',
                      },
                      {
                        value: 'avg',
                        label: 'Среднее значение',
                      },
                      {
                        value: 'count',
                        label: 'Количество',
                      },
                    ]}
                  />
                )}
              />

              <ErrorMessage
                name='action_type'
                errors={form.formState.errors}
                render={({ message }) => (
                  <Text color={'#FF2802'} fontSize={12}>
                    {message}
                  </Text>
                )}
              />
            </FilterFormControl>
            <FilterFormControl title='Поле'>
              <Controller
                control={form.control}
                name='target_field'
                rules={{
                  required: {
                    message: 'Обязательно выберите операцию',
                    value: true,
                  },
                }}
                render={({ field: { value, onChange } }) => (
                  <Select
                    value={value}
                    onChange={onChange}
                    styles={{
                      container: (provided) => ({
                        ...provided,
                        width: '100%',
                      }),
                    }}
                    placeholder='Выберите поле'
                    options={[
                      {
                        value: 'credit_sum',
                        label: 'Сумма кредита',
                      },
                      {
                        value: 'payment_amount',
                        label: 'Внесенные средства',
                      },
                      {
                        value: 'made_payments',
                        label: 'Сделанные платежи',
                      },

                      {
                        value: 'calculated_payment_number',
                        label: 'Срок кредита',
                      },
                    ]}
                  />
                )}
              />

              <ErrorMessage
                name='target_field'
                errors={form.formState.errors}
                render={({ message }) => (
                  <Text color={'#FF2802'} fontSize={12}>
                    {message}
                  </Text>
                )}
              />
            </FilterFormControl>
            <FilterFormControl title='Дата погашения'>
              <HStack>
                <Input
                  type='date'
                  border={'1px solid #B1B1B1'}
                  placeholder='С...'
                  {...form.register('closed_at_from')}
                />
                <Input
                  type='date'
                  border={'1px solid #B1B1B1'}
                  placeholder='По...'
                  {...form.register('closed_at_to')}
                />
              </HStack>
            </FilterFormControl>

            <FilterFormControl title='Срок кредита'>
              <HStack>
                <Input
                  type='number'
                  border={'1px solid #B1B1B1'}
                  placeholder='Мин срок.'
                  {...form.register('calculated_payment_number_from', {
                    valueAsNumber: true,
                    min: 0,
                  })}
                />
                <Input
                  type='number'
                  border={'1px solid #B1B1B1'}
                  placeholder='Макс. срок.'
                  {...form.register('calculated_payment_number_to', {
                    valueAsNumber: true,
                    min: 0,
                  })}
                />
              </HStack>
            </FilterFormControl>

            <FilterFormControl title='Кол-во платежей'>
              <HStack>
                <Input
                  type='number'
                  border={'1px solid #B1B1B1'}
                  placeholder='Мин кол-во.'
                  {...form.register('made_payments_from', {
                    valueAsNumber: true,
                    min: 0,
                  })}
                />
                <Input
                  type='number'
                  border={'1px solid #B1B1B1'}
                  placeholder='Макс. кол-во.'
                  {...form.register('made_payments_to', {
                    valueAsNumber: true,
                    min: 0,
                  })}
                />
              </HStack>
            </FilterFormControl>

            <FilterFormControl title='Сумма кредита'>
              <HStack>
                <Input
                  type='number'
                  border={'1px solid #B1B1B1'}
                  placeholder='Мин сум.'
                  {...form.register('credit_sum_from', {
                    valueAsNumber: true,
                    min: 0,
                  })}
                />
                <Input
                  type='number'
                  border={'1px solid #B1B1B1'}
                  placeholder='Макс. сум.'
                  {...form.register('credit_sum_to', {
                    valueAsNumber: true,
                    min: 0,
                  })}
                />
              </HStack>
            </FilterFormControl>
            <Button type='submit' w={'100%'} bg={'#FF5602'} color={'white'}>
              Применить
            </Button>
          </VStack>
        </FormBaseLayout>
      </VStack>
    </>
  );
};
