class Dog(object):

    @staticmethod
    def run():
        
        # 不访问实例属性/类属性
        print("小狗要跑...")

# 通过类名.调用静态方法 - 不需要创建对象
# 直接调用类名，不需要创建对象实例化
# 相比前面017的类方法，方法前面加一个装饰器后，实例都不用创建


Dog.run()
