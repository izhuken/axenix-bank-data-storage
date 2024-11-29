import { CredentialOptions } from './types';

class _CredentialStorage {
  get(key: string): string | null {
    const matches = document.cookie.match(
      new RegExp(
        '(?:^|; )' +
          key.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') +
          '=([^;]*)',
      ),
    );
    return matches ? decodeURIComponent(matches[1]) : null;
  }
  getAll() {
    const cookies = document.cookie
      .split('; ')
      .map((cookString) => cookString.split('='));
    let data = {};

    cookies.forEach((cookie) => {
      data = { ...data, ...{ [cookie[0]]: cookie[1] } };
    });

    return data;
  }

  set(key: string, value: string, options: CredentialOptions = {}): void {
    const expiresDate = new Date();
    expiresDate.setDate(expiresDate.getDate() + 7);

    options.expires = expiresDate;

    if (options && options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
    }
    let updatedCookie = `${encodeURIComponent(key)}=${encodeURIComponent(
      value,
    )}; path=/;`;

    for (const [optionKey, optionValue] of Object.entries(options)) {
      let usableKey = optionKey;

      if (optionKey === 'maxAge') {
        usableKey = 'max-age';
      }

      updatedCookie += '; ' + usableKey;

      if (optionValue !== true) {
        updatedCookie += '=' + optionValue;
      }
    }

    document.cookie = updatedCookie;
  }

  delete(key: string): void {
    this.set(key, '', {
      maxAge: -1,
    });
  }

  invalidate(): void {
    const cookies = this.getAll();
    Object.keys(cookies).forEach((name) => this.delete(name));
  }
}

export const CredentialStorage = new _CredentialStorage();
