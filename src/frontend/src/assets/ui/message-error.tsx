import clsx from 'clsx';
import React from 'react';
import { DefaultStyle } from '..';

interface MessageErrorProps {
  message: string;
}

export const MessageError: React.FC<MessageErrorProps> = ({ message }) => {
  return (
    <div className={clsx(DefaultStyle.error, DefaultStyle.message)}>
      <img src='/message-alert.svg' alt='Alert' />
      {message}
    </div>
  );
};
