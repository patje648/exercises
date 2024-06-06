from abc import ABC, abstractmethod
import re
class StorageDevice:
    def __init__(self,block_count, block_size):
        self.block_count=block_count
        self.__block_size=block_size
        self.__available_blocks={}
        self.__used_blocks={}

    @property
    def available_block_count(block_count):
        return block_count
    
    @property
    def used_block_count(__used_blocks):
        return __used_blocks
    
    @property
    def total_block_count(block_count):
        return block_count+__used_blocks # type: ignore
    
    @property
    def block_size(__block_size):
        return __block_size
    
    def take_blocks(self, block_count):
        if block_count > len(self.__available_blocks):
            raise RuntimeError("Insufficient available blocks")

        blocks = list(self.__available_blocks.keys())[:block_count]
        for block in blocks:
            self.__used_blocks[block] = self.__available_blocks.pop(block)

        return blocks

    def free(self, blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError("Block {} is not in used blocks".format(block))
            self.__available_blocks[block] = self.__used_blocks.pop(block)

class Entity:
    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError("Invalid name")
        self.__storage = storage
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise RuntimeError("Invalid name")
        self.__name = new_name

    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size

    @abstractmethod
    def clear(self):
        pass

class File(Entity):
    @staticmethod
    def is_valid_name(name):
        # Add your implementation here
        pass

    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError("Invalid name")
        self.__storage = storage
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise RuntimeError("Invalid name")
        self.__name = new_name

    @property
    def storage(self):
        return self.__storage

    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size

    @abstractmethod
    def clear(self):
        pass