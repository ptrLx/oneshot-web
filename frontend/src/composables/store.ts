import { OneShotRespDTO } from '@/_generated/api-client';
import { reactive } from 'vue';

export const store = reactive({
    profilePicUpdate: 0,
    notifyProfilePicUpdate() {
        this.profilePicUpdate++;
    },
});

export const blobStore = reactive({
    blob: new Blob(),
    setBlob(blob: Blob) {
        this.blob = blob;
    },
    getBlob() {
        return this.blob;
    }
})

export const metadataStore = reactive({
    metadata: {} as OneShotRespDTO,
    setMetadata(metadata: OneShotRespDTO) {
        this.metadata = metadata;
    },
    getMetadata() {
        return this.metadata;
    }
})

export const theme = reactive({
    theme: '',
    setTheme(theme: string) {
        this.theme = theme;
    },
    getTheme() {
        return this.theme;
    },
    isSet() {
        return this.theme !== '';
    }
})