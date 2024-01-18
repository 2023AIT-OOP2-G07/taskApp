const work_form_minute = document.getElementById("work_form_minute");
const work_form_second = document.getElementById("work_form_second");
const rest_form_minute = document.getElementById("rest_form_minute");
const rest_form_second = document.getElementById("rest_form_second");
const start_stop_button = document.getElementById("start_stop_button");
const reset_button = document.getElementById("reset_button");
const mode_change_button = document.getElementById("mode_change_button");
const clear_log_button = document.getElementById("clear_log_button");
const save_log_button = document.getElementById("save_log_button");
const display_minute =  document.getElementById("display_minute");
const display_second =  document.getElementById("display_second");
const display_status =  document.getElementById("display_status");
const apply_form_buttons = document.getElementsByClassName("apply_form");
const log_box = document.getElementById("log_box")

class Timer {
    constructor(min, sec, working, timerId, posing, must_change){
        this.min = min; //分を保持するメンバ変数
        this.sec = sec; //秒を保持するメンバ変数
        this.working = working; //状態をブール型で保持する
        this.timerId = timerId; //countdownに使っているIntervalのIDを保持
        this.posing = posing; //一時停止中かどうかをブーリアン値で保持 
        this.must_change = must_change //モードチェンジすべきかどうかをブーリアン値で保持 また集中モード、休憩モード開始前もtrue
    }

    countdown(){ //メンバ変数 min==0, sec=0になるまでカウントダウンする。00:00になったらモードをチェンジする
        if(this.sec != 0){ //秒が0でないときに実行
            this.sec = this.sec - 1;
        }else{ //秒が0のときに実行
            if(this.min == 0){ //00:00のときの処理
                if(this.working){
                    log.add_log(get_date() + " に作業["+ work_form_minute.value + ":" + work_form_second.value + "]を完了");
                }else{
                    log.add_log(get_date() + " に休憩["+ rest_form_minute.value + ":" + rest_form_second.value + "]を完了");
                }
                this.mode_change();
            }else{
                this.min = this.min - 1;
                this.sec = 59;
            }
        }
    }

    inquire_form(){ //timerのメンバ変数 min, secをフォームの数値に合わせる
        if(this.working){//集中モード中の時は「集中」のフォームから値を取得
            this.min = work_form_minute.value;
            this.sec = work_form_second.value;
        }else if(!this.working){//休憩モード中の時は「休憩」のフォームから値を取得
            this.min = rest_form_minute.value;
            this.sec = rest_form_second.value;
        }
    }

    update_display(){ //timerをhtmlに表示させる
        if(this.working){
            display_status.textContent = "WORKING";
            display_minute.textContent = this.min;
            display_second.textContent = this.sec;
        }else if(!this.working){
            display_status.textContent = "RESTING";
            display_minute.textContent = this.min;
            display_second.textContent = this.sec;
        }
    }

    mode_change(){ //モードを切り替える
        if(this.working){ //集中モードのとき
            this.working = false; //休憩モードへ移行
        }else{ //休憩モードのとき
            this.working = true; //集中モードへ移行
        }
        //change_background_color(); //背景色を変更
        this.inquire_form(); //時間を取得
        this.update_display(); //時間をhtmlに表示
        start_stop_button.textContent = "スタート";
        this.must_change = true;
        this.posing = false;
        clearInterval(this.timerId);
    }
}

function handleTimer(){
    if((timer.working && !timer.posing && !timer.must_change) || (!timer.working && !timer.posing && !timer.must_change)){ //集中モード中 休憩モード中
        timer.countdown();
        //タイマー表示を書き換える
        timer.update_display();
    }

}

function handle_clicked_start_stop_button(){
    if(timer.working && !timer.posing && timer.must_change){ //集中開始前に押された場合(作業開始のタイミング)
        timer.working = true; //集中モードに変更
        timer.must_change = false;
        timer.inquire_form(); //timerにformの時間をセット
        timer.timerId = setInterval("handleTimer()", 1000);
        start_stop_button.textContent = "ストップ";
        log.add_log(get_date() + " に作業["+ work_form_minute.value + ":" + work_form_second.value + "]を開始");
    }else if(timer.working && !timer.posing && !timer.must_change){ //集中モード中に押された場合(作業一時停止のタイミング)
        clearInterval(timer.timerId);
        timer.posing = true;
        start_stop_button.textContent = "スタート";
        log.add_log(get_date() + " に作業["+ work_form_minute.value + ":" + work_form_second.value + "]を一時停止");
    }else if(timer.working && timer.posing && !timer.must_change){ //集中モード中の一時停止中に押された場合(作業再開のタイミング)
        timer.posing = false;
        timer.timerId = setInterval("handleTimer()", 1000);
        start_stop_button.textContent = "ストップ";
        log.add_log(get_date() + " に作業["+ work_form_minute.value + ":" + work_form_second.value + "]を再開");
    }else if(!timer.working && !timer.posing && timer.must_change){ //休憩モード開始前に押された場合(休憩開始のタイミング)
        timer.working = false; //休憩モードに変更
        timer.must_change = false;
        timer.inquire_form(); //timerにformの時間をセット
        timer.timerId = setInterval("handleTimer()", 1000);
        start_stop_button.textContent = "ストップ";
        log.add_log(get_date() + " に休憩["+ rest_form_minute.value + ":" + rest_form_second.value + "]開始");
    }else if(!timer.working && !timer.posing && !timer.must_change){ //休憩モード中に押された場合(休憩一時停止のタイミング)
        clearInterval(timer.timerId);
        timer.posing = true;
        start_stop_button.textContent = "スタート";
        log.add_log(get_date() + " に休憩["+ rest_form_minute.value + ":" + rest_form_second.value + "]を一時停止");
    }else if(!timer.working && timer.posing && !timer.must_change){ //休憩モード中の一時停止中に押された場合(休憩再開のタイミング)
        timer.posing = false;
        timer.timerId = setInterval("handleTimer()", 1000);
        start_stop_button.textContent = "ストップ";
        log.add_log(get_date() + " に休憩["+ rest_form_minute.value + ":" + rest_form_second.value + "]を再開");
    }
}

function handle_clicked_reset_button(){
    timer.must_change = true;
    timer.posing = false;
    start_stop_button.textContent = "スタート";
    log.add_log(get_date() + " にタイマーをリセット");
    clearInterval(timer.timerId);
    timer.inquire_form();
    timer.update_display()
}

function handle_clicked_mode_change_button(){ // 集中モード、休憩モードの開始時または、一時停止中に実行できる
    if( (timer.working && !timer.posing && timer.must_change) || (!timer.working && !timer.posing && timer.must_change) || (timer.working && timer.posing && !timer.must_change) || (!timer.working && timer.posing && !timer.must_change) ){
        if(timer.working){
            log.add_log(get_date() + " に作業から休憩へチェンジ");
        }else{
            log.add_log(get_date() + " に休憩から作業へチェンジ");
        }
        
        timer.mode_change();

    }
}

function handle_clicked_apply_button(){ // 集中モード、休憩モードの開始時または、一時停止中に実行できる
    if( (timer.working && !timer.posing && timer.must_change) || (!timer.working && !timer.posing && timer.must_change) || (timer.working && timer.posing && !timer.must_change) || (!timer.working && timer.posing && !timer.must_change) ){
        timer.inquire_form();
        timer.update_display();
    }
}

function change_background_color(){
    if(timer.working){ //集中モード中のとき,背景を赤に変える
        document.body.style.backgroundColor = "rgb(211, 165, 170)";
        document.getElementById("translator").style.backgroundColor = "rgb(223, 177, 182)";
        document.getElementById("todo").style.backgroundColor = "rgb(223, 177, 182)";
        document.getElementById("cats").style.backgroundColor = "rgb(223, 177, 182)";
    } else if(!timer.working){ //集中モード中のとき,背景を赤に変える
        document.body.style.backgroundColor = "rgb(165, 203, 211)";
        document.getElementById("translator").style.backgroundColor = "rgb(178, 218, 226)";
        document.getElementById("todo").style.backgroundColor = "rgb(178, 218, 226)";
        document.getElementById("cats").style.backgroundColor = "rgb(178, 218, 226)";
    }
}

class Log{
    constructor(log_data){
        //web側のlogboxには、log_dataの文字列が表示される
        this.log_data = log_data;
    }
    
    //web側の表示をlog_dataの値で上書きする
    update_display(){
        log_box.innerText = this.log_data;
        console.log("nekotest")
        log_box.scroll(0,log_box.scrollHeight);
    }

    //web側、システム側の両方にログを追加する
    add_log(log_content){
        this.log_data += log_content + "\n" ;
        this.update_display();
    }

    //web側、システム側両方から完全にログを削除する
    clear_log(){
        this.log_data = "";
        this.update_display();
    }

    get_log_json(){
        let data = {
            "log" : log.log_data
        }
        return data;
    }
}

function handle_clicked_clear_log_button(){ // ログを削除する
    log.clear_log()
}

function get_date(){
    var date = new Date();
    return date.getFullYear() + '/' + ('0' + (date.getMonth() + 1)).slice(-2) + '/' 
    +('0' + date.getDate()).slice(-2) + ' ' +  ('0' + date.getHours()).slice(-2) + ':' + 
    ('0' + date.getMinutes()).slice(-2) + ':' + ('0' + date.getSeconds()).slice(-2);
}

//flaskへGETし、受け取ったjsonデータを返す関数
function get2flask(){
    let json_data;
    fetch("ここにアドレス", {method: "GET"})
        .then(response => response.json())
        .then(json => json_data = json)
    return json_data;
}

//引数で受け取ったjsonをflaskへ送る関数
function post2flask(json){
    fetch('/ここにアドレス', {
        method: 'POST',
        body: json, 
        }).then((response) => {
        // 正常に通信できるとここが実行されますが、今回はサーバー側を作っていないため、下のエラーへ必ず行きます
        return false
        }).catch(error => {
        console.error(error)
    })
}

//ログをjsonにまとめflaskへ送る処理を実行する関数
function save_log(){
    data = log.get_log_json();
    post2flask(data);
    console.log(data)
}

// ------------------↑↑↑↑↑ 関数やクラスの定義　↑↑↑↑↑-----------------------
// ------------------↓↓↓↓↓ 起動時に実行　↓↓↓↓↓-----------------------

json = get2flask();
// ** saved_log = json["log"];

//　イベントを仕込む
start_stop_button.addEventListener("click", handle_clicked_start_stop_button);
reset_button.addEventListener("click", handle_clicked_reset_button);
mode_change_button.addEventListener("click", handle_clicked_mode_change_button);
for(let i=0; i<2; i++){
    apply_form_buttons[i].addEventListener("click", handle_clicked_apply_button);
}
clear_log_button.addEventListener("click", handle_clicked_clear_log_button);
save_log_button.addEventListener("click", save_log);


// インスタンスtimerの初期設定
const init_min = work_form_minute.value
const init_sec = work_form_second.value
const timer = new Timer(init_min, init_sec, 10, null, false, true);
//web側のタイマー表示の初期設定
timer.update_display();

// logの初期設定
// 88 const log = new Log(saved_log);  
const log = new Log("");

