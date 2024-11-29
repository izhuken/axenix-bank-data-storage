import clsx from 'clsx';
import { FC } from 'react';
import { DefaultStyle } from '..';

interface LoaderProps {
  inverse?: boolean;
}

export const Loader: FC<LoaderProps> = ({ inverse }) => {
  return (
    <span
      className={clsx(DefaultStyle.loader, inverse ? DefaultStyle.white : '')}
    ></span>
  );
};
