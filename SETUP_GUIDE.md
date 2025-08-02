# دليل الإعداد السريع لمتجر التمور الجزائرية 🚀

## للتشغيل على Replit

### الخطوة 1: إنشاء مشروع جديد
1. اذهب إلى [Replit.com](https://replit.com)
2. اضغط على "Create Repl"
3. اختر "Import from GitHub" أو "Upload files"

### الخطوة 2: رفع الملفات
ارفع جميع الملفات التالية إلى Replit:
- `main.py` (ملف التشغيل الرئيسي)
- `requirements.txt` (متطلبات Python)
- `src/` (مجلد الكود المصدري)
- `.replit` (ملف تكوين Replit)
- `replit.nix` (ملف التبعيات)

### الخطوة 3: التشغيل
1. اضغط على زر "Run" الأخضر
2. انتظر حتى يتم تثبيت المتطلبات
3. سيفتح المتجر في نافذة جديدة

## إضافة البيانات التجريبية

بعد تشغيل المشروع، قم بزيارة:
```
https://your-repl-name.your-username.repl.co/api/init-data
```

أو استخدم curl:
```bash
curl -X POST https://your-repl-name.your-username.repl.co/api/init-data
```

## استكشاف الأخطاء

### مشكلة: لا يعمل التطبيق
**الحل**: تأكد من وجود ملف `main.py` في الجذر

### مشكلة: خطأ في المتطلبات
**الحل**: تأكد من وجود ملف `requirements.txt` وأنه يحتوي على:
```
Flask==3.1.1
Flask-SQLAlchemy==3.1.1
Flask-CORS==6.0.0
```

### مشكلة: لا تظهر الصور
**الحل**: تأكد من وجود مجلد `src/static/assets/` مع الصور

## الميزات المتاحة

✅ عرض المنتجات  
✅ إضافة للسلة  
✅ إدارة الطلبات  
✅ واجهة عربية  
✅ تصميم متجاوب  
✅ API متكامل  

## روابط مفيدة

- [توثيق Flask](https://flask.palletsprojects.com/)
- [توثيق React](https://react.dev/)
- [دعم Replit](https://docs.replit.com/)

---

**نصيحة**: احفظ رابط المشروع بعد النشر لسهولة الوصول إليه لاحقاً!

