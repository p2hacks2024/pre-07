<script>
import SelectPostView from '@/components/SelectPostView.vue'
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            ids: [],
            selectedItems: [],
            rotate_angle: 0,
            isMixMode: false,
            showPlalette: false,
            radius: 120,
            palette_data : {
                title: '',
                content: '',
            },
            apititle: '', // 追加
            apidetail: '', // 追加
            apiImage: '', // 追加
            endpoint: endpoint,
            isLoading: false // 追加
        }
    },
    methods: {
        handleItemClick(item, title, description) {
            this.selectedItems.push({ item, title, description});
            console.log(this.selectedItems);
        },
        getCirclePosition(index, total)  {
            if (total === 0) return { left: '50%', top: '50%' }
            const angle = (index * 360 / total) - 90 + this.rotate_angle
            const x = Math.cos((angle * Math.PI) / 180) * this.radius
            const y = Math.sin((angle * Math.PI) / 180) * this.radius
            return {
                left: `calc(50% + ${x}px)`,
                top: `calc(50% + ${y}px)`
            }
        },
        async handleMixMode() {
            console.log('mix mode')
            this.isMixMode = true
            this.isLoading = true; // 追加

            // selectedItemsのtitleとdescriptionをカンマ区切りの文字列にして出力
            const itemsString = this.selectedItems.map(item => `${item.title}%2C${item.description}`).join('%2C');
            console.log(itemsString);

            try {
                const response = await fetch(endpoint+'mix?keyword='+itemsString, {
                    method: 'GET',
                    credentials: 'include'
                });
                const data = await response.json();
                this.apititle = data.title; // 取得したデータをapiResultに格納
                this.apidetail = data.detail; // 取得したデータをapiResultに格納
                this.apiImage = data.image; // 取得したデータをapiImageに格納
            } catch (error) {
                console.error('API fetch error:', error);
            } finally {
                this.isLoading = false; // 追加
            }
        },
    },
    async created() {
        try {
            const response = await fetch(endpoint + 'palette/', {
            method: 'GET',
            credentials: 'include'
        })
        const data = await response.json()
        this.ids = data
        } catch (error) {
            console.error('API fetch error:', error)
        }
    },
    mounted() {
        setInterval(() => {
            this.rotate_angle += 0.3;
            if (this.isMixMode) {
                if (this.radius >= 0) {
                    this.radius -= 1;
                }
                else {
                    this.showPlalette = true
                }
            }
        }, 10); // 1秒ごとにrotate_angleを1増加
    }
}
</script>

<template>
    <div class="timeLine">
        <div v-for="id in ids" :key="id" class="postContents">
            <SelectPostView class="postView" :id="id" @item-click="handleItemClick"/>
        </div>
        <div :class="{ 'overlay': isMixMode }"></div>

        <div class="palette" :class="{'palette-show': showPlalette}">
            <div v-if="isLoading">Generating...</div> <!-- 追加 -->
            <div v-else>
                <img :src="`${endpoint}image/${apiImage}`" alt="palette" />
                <div class="palette-text">
                    <h2>{{ apititle }}</h2>
                    <p>{{ apidetail }}</p>
                </div>
                <div class="regenerate" @click="handleMixMode">
                    再生成
                </div>
            </div>
        </div>

        <div class="circle" :class="{ 'center-move': isMixMode }">
            <div v-for="(item, index) in selectedItems" :key="index" :style="getCirclePosition(index, selectedItems.length)" class="item">
                {{ item.title }}
            </div>
            <img class="center-circle" src="@/assets/balloon.png" alt="circle" @click="handleMixMode">
        </div>
    </div>
</template>

<style scoped>
.timeLine {
    background-color: #f3f3f3;
    display: flex;
    flex-wrap: wrap;
}
.palette {
    display: none;
}
.palette-show {
    display: block;
    position: fixed;
    top: 8%;
    left: 10%;
    width: 70%;
    max-height: 80%;
    background-color: rgb(255, 255, 255);
    z-index: 12;
    border-radius: 10px;
    padding: 5%;
    word-break: break-all;
}
.palette img {
    width: 100%;
    height: 100%;
    border-radius: 20px;
}
.palette .palette-text {
    max-height: 270px; /* 追加: 最大高さを設定 */
    overflow-y: auto; /* 追加: スクロール可能にする */
}
.regenerate {
    margin-top: 20px;
    padding: 10px 30px ;
    border-radius: 10px;
    float: right;
    box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.462);
}
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 10;
}
.postContents {
    width: 100%;
}

.postView {
    margin: 10px;
}
.circle {
    position: fixed;
    left: 50%;
    top: 75%;
    transform: translateX(-65px) translateY(-65px);
    z-index: 11;
}
.center-circle {
    width: 130px;
    height: 130px;
    /* transform: translateX(-225px) translateY(-250px); */
    opacity: 0.9;
}
.center-move {
    transform: translate(-50%, -50%);
    transition: transform 1s ease;
    position: fixed;
    top: 50%;
    left: 50%;
}

.item {
    position: absolute;
    width: 80px;
    height: 80px;
    transform: translateX(-40px) translateY(-40px);
    border-radius: 50%;
    background-color: rgba(239, 239, 239, 0.834);
    color: #000;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    cursor: pointer;
}
</style>