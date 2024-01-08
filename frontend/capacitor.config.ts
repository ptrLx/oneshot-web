import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'de.ptrlx.oneshot-web',
  appName: 'OneShot Web',
  webDir: 'dist',
  server: {
    androidScheme: 'http', // do not change this to https. Otherwise the connection (android emulator - local api) will not work anymore.
    hostname: 'localhost',
  }
};

export default config;
