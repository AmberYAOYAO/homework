class Router:
    def db_for_read(self,model,**hints):
        """返回用于读的数据库"""
        return "salve"

    def db_for_write(self,model,**hints):
        """返回用于写的数据库"""
        return "default"

    def allow_relation(self,obj1,obj2,**hints):
        """允许混合操作"""
        return True