import asyncio
from typing import (Type, Optional, Any, TypedDict)
from abc import abstractmethod


class AbstractConnection:

	__slots__ = (
		"host",
		"port",
		"user",
		"password",
		"namespace",
		"db"
	)

	def __init__(
			self,
			*,
			host: str = "localhost",
			port: int = 8000,
			user: str,
			password: str,
			namespace: Optional[str] = None,
			db: Optional[str] = None
	):
		self.host = host
		self.port = int(port)
		self.user = user
		self.password = password
		self.namespace = namespace
		self.db = db

	@abstractmethod
	async def _connect(self):
		pass


class Connection(AbstractConnection):

	def __init__(
			self,
			*,
			host: str = "localhost",
			port: int = 8000,
			user: str,
			password: str,
			namespace: Optional[str] = None,
			db: Optional[str] = None,
			**kwargs
	):
		self.host = host
		self.port = int(port)
		self.user = user
		self.password = password
		self.namespace = namespace
		self.db = db
		super().__init__(**kwargs)

