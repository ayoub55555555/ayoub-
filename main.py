#!/usr/bin/env python3
"""
متجر التمور الجزائرية الإلكتروني
Algerian Dates E-commerce Store

تطبيق Flask لمتجر إلكتروني لبيع التمور الجزائرية
مع واجهة أمامية React مدمجة
"""

import os
import sys

# إضافة مسار src إلى Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.main import app

if __name__ == '__main__':
    # تشغيل التطبيق على المنفذ المحدد من Replit أو 5000 افتراضياً
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

