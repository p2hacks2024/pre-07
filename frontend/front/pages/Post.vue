<template>
    <div class="form-container">
        <form @submit.prevent="handleSubmit">
            <div class="input-group">
                <label for="idea-name">アイデア名</label>
                <input
                    type="text"
                    id="idea-name"
                    v-model="idea.name"
                    placeholder="アイデア名を入力"
                    required
                />
            </div>

            <div class="input-group">
                <label for="idea-description">アイデアの説明</label>
                <textarea
                    id="idea-description"
                    v-model="idea.description"
                    placeholder="アイデアの詳細を記入"
                    rows="4"
                    required
                ></textarea>
            </div>

            <!-- 画像のアップロード -->
            <div class="input-group upload-group">
                <label for="image-upload">画像のアップロード(任意)</label>
                <input
                    type="file"
                    id="image-upload"
                    @change="handleFileUpload"
                    accept="image/*"
                />
                <div class="upload-placeholder" v-if="!uploadedImage">
                    <span><img src="@/assets/photo.png" alt="photo"></span>
                </div>
                <img
                    v-else
                    :src="uploadedImage"
                    alt="Uploaded preview"
                    class="uploaded-image"
                />
            </div>

            <!-- 投稿ボタン -->
            <button type="submit" class="submit-button">
                <!-- <img src="@/assets/light.png" alt="human" /> -->
                投稿
            </button>
        </form>
    </div>
</template>

<script>
import { endpoint } from '~/components/APIEndPoint';
export default {
    data() {
        return {
            idea: {
                name: "",
                description: "",
            },
            uploadedImage: null,
        };
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.uploadedImage = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        },
        handleSubmit() {
            console.log("アイデア送信:", this.idea);
            if (this.uploadedImage) {
                console.log("アップロード画像:", this.uploadedImage);
            }

            const formData = new FormData();
            if (this.uploadedImage) {
                const blob = this.dataURLtoBlob(this.uploadedImage);
                formData.append('file', blob, 'uploaded-image.png');
            }

            fetch('https://p2hacks.ict-lab.org/api/idea?title='+this.idea.name+"&description="+this.idea.description, {
                method: 'POST',
                headers: {
                    'accept': 'application/json',
                },
                credentials: 'include',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                this.$router.push('/idea/' + data.idea_id);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        },
        dataURLtoBlob(dataURL) {
            const byteString = atob(dataURL.split(',')[1]);
            const mimeString = dataURL.split(',')[0].split(':')[1].split(';')[0];
            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            return new Blob([ab], { type: mimeString });
        },
    },
};
</script>

<style scoped>
/* フォームコンテナ */
.form-container {
    padding: 5%;
    max-width: 400px;
    margin: 0 auto;
    background: #fff;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80vh;
}

/* ラベルと入力フィールド */
.input-group {
    margin-bottom: 20px;
}

.input-group label {
    display: block;
    font-size: 14px;
    margin-bottom: 5px;
    text-align: left;
}

.input-group input,
.input-group textarea {
    width: 100%;
    padding: 15px 30px;
    font-size: 14px;
    border: 1px solid #ffffff;
    background-color: #f5f5f5;
    border-radius: 15px;
    box-sizing: border-box;
    text-align: center;
    color: #000000;
}

/* アップロードエリア */
.upload-group {
    text-align: center;
}

.upload-placeholder {
    width: 100px;
    height: 100px;
    margin: 10px auto;
    border: 2px dashed #ccc;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    font-size: 24px;
    cursor: pointer;
}

.uploaded-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border-radius: 10px;
    margin: 10px auto;
}



/* ボタン */
.submit-button {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    background: #FFF7A1;
    color: #000;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.submit-button span {
    margin-right: 8px;
}

.submit-button:hover {
    background: #fdf5a0;
}
</style>
