// 要素を取得
const memoBtn = document.querySelector("#memo_button");
const memoTxt = document.querySelector("#memo_text");
const memoEdit_list = document.querySelectorAll(".memo_edit");

// 初期値
const memo_init_text = "タイトルを入力";

// ページ読み込み時の処理
function docDOMContentLoaded(e) {
  memoTxt.value = memo_init_text;
}

// メモボタンクリック時の処理
function memoBtnClick(e) {
  if (memoTxt.value === memo_init_text) return;

  const memoCreateForm = document.querySelector(".memo_create_form");
  const memoTitle = document.querySelector(".memo_title");
  const memoTitleHidden = document.querySelector(".memo_title_hidden");
  const memoList = document.querySelector(".memo_list");

  memoCreateForm.style.display = "inline";
  memoTitle.textContent = memoTitleHidden.value = memoTxt.value;
  memoList.style.display = "none";
}

// メモテキストクリック時の処理
function memoTxtClick(e) {
  if (memoTxt.value === memo_init_text) memoTxt.value = "";
}

// メモ入力フォーカスが外れた時の処理
function memoTxtBlur(e) {
  if (memoTxt.value === "") memoTxt.value = memo_init_text;
}
// メモ入力時にキーが押された時の処理
function memoTxtKeydown(e) {
  if (e.key === "Enter") memoBtn.click();
}

// メモ編集ボタンクリック時の処理
function memoEditBtn(e) {
  const memoEdit = document.querySelector(".memo_key");
  const key = memoEdit.value;
  console.log(key);
}

// イベントリスナーを設定
document.addEventListener('DOMContentLoaded', docDOMContentLoaded);
memoBtn.addEventListener("click", memoBtnClick);
memoTxt.addEventListener("click", memoTxtClick);
memoTxt.addEventListener("blur", memoTxtBlur)
memoTxt.addEventListener("keydown", memoTxtKeydown);
for (const memoEdit of memoEdit_list) memoEdit.addEventListener("click", memoEditBtn);